import strawberry
from typing import List
from .engine import calculate_score

@strawberry.input
class ReconciliationItem:
    id: str
    amount: float
    date: str # ISO string
    description: str

@strawberry.type
class MatchResult:
    invoice_id: str
    transaction_id: str
    score: float
    explanation: str

@strawberry.type
class Query:
    @strawberry.field
    def suggest_matches(
        self, 
        invoices: List[ReconciliationItem], 
        transactions: List[ReconciliationItem]
    ) -> List[MatchResult]:
        results = []

        for inv in invoices:
            # Parse dates once per invoice
            inv_dt = datetime.fromisoformat(inv.date.replace('Z', '+00:00'))
            
            for tx in transactions:
                tx_dt = datetime.fromisoformat(tx.date.replace('Z', '+00:00'))
                
                score, explanation = calculate_score(
                    inv.amount, tx.amount, 
                    inv_dt, tx_dt, 
                    inv.description, tx.description
                )

                # Only return high-confidence matches (e.g., > 0.4)
                if score >= 0.4:
                    results.append(MatchResult(
                        invoice_id=inv.id,
                        transaction_id=tx.id,
                        score=score,
                        explanation=explanation
                    ))

        # Sort results by score descending
        return sorted(results, key=lambda x: x.score, reverse=True)

schema = strawberry.Schema(query=Query)