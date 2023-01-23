with source as (
      select * from {{ source('public', 'Person') }}
),
renamed as (
    select
        *
    from source
)
select * from renamed
