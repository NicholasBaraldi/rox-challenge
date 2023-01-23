with source as (
      select * from {{ source('public', 'Product') }}
),
renamed as (
    select
        *
    from source
)
select * from renamed
