# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleCloudBigquery(PythonPackage):
    """Querying massive datasets can be time consuming and expensive without the right hardware and infrastructure. Google BigQuery solves this problem by enabling super-fast, SQL queries against append-mostly tables, using the processing power of Google's infrastructure."""

    homepage = "https://github.com/googleapis/python-bigquery"
    pypi = "google-cloud-bigquery/google-cloud-bigquery-3.13.0.tar.gz"

    version("3.13.0", sha256="794ccfc93ccb0e0ad689442f896f9c82de56da0fe18a195531bb37096c2657d6")

    depends_on("py-google-api-core", type=("build", "run"))
    depends_on("py-google-cloud-core", type=("build", "run"))
    depends_on("py-google-resumable-media", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-dateutil", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-google-cloud-bigquery-storage@2.6.0:", type=("build", "run"))
    depends_on("py-pandas@1.1.0:", type=("build", "run"))
    depends_on("py-pyarrow+parquet@3.0.0:", type=("build", "run"))
    depends_on("py-db-dtypes@0.3.0:2.0.0", type=("build", "run"))
    depends_on("py-ipywidgets@7.7.0", type=("build", "run"))
    depends_on("py-ipykernel@6.0.0:", type=("build", "run"))
    depends_on("py-geopandas@0.9.0:", type=("build", "run"))
    depends_on("py-shapely@1.8.4:3.0.0", type=("build", "run"))
    depends_on("py-ipython@7.23.1:", type=("build", "run"))
    depends_on("py-tqdm@4.7.4:", type=("build", "run"))
    depends_on("py-opentelemetry-api@1.1.0:", type=("build", "run"))
    depends_on("py-opentelemetry-sdk@1.1.0:", type=("build", "run"))
    depends_on("py-opentelemetry-instrumentation@0.20b0:", type=("build", "run"))
    depends_on("py-proto-plus@1.15.0:2.0.0", type=("build", "run"))
    depends_on("py-protobuf@3.19.5:5.0.0", type=("build", "run"))
