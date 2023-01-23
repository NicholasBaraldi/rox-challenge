with source as (
      select * from {{ source('public', 'SalesOrderHeader') }}
),
renamed as (
    select
        *
    from source
)
select * from renamed
