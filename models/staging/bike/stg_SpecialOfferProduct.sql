with source as (
      select * from {{ source('public', 'SpecialOfferProduct') }}
),
renamed as (
    select
        *
    from source
)
select * from renamed
