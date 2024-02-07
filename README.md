# financial-report-analyzer

Pull Postgres image::

    docker pull postgres


Start Postgres Container::

    docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
