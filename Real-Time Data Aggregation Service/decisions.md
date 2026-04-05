
# Decisions

## APIs

Primary: Open ER API
Fallback: ExchangeRate Host

## Strategy

Try primary
Try fallback
Return cache

## Staleness

Fresh <5 min
Stale >30 min

## Cuts

No auth
No DB
No charts

## Future

Redis cache
Premium routing
Charts
