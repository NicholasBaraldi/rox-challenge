with source as (
      select * from {{ source('public', 'SalesOrderDetail') }}
),
renamed as (
    select
        *
    from source
)
select * from renamed
