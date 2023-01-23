with source as (
      select * from {{ source('public', 'Customer') }}
),
renamed as (
    select
        *
    from source
)
select * from renamed
