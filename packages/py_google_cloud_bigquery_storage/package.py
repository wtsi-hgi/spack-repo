# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleCloudBigqueryStorage(PythonPackage):
    """Python Client for Google BigQuery Storage API."""

    homepage = "https://github.com/googleapis/python-bigquery-storage"
    pypi = "google-cloud-bigquery-storage/google-cloud-bigquery-storage-2.22.0.tar.gz"

    version("2.22.0", sha256="f6d8c7b3ab9b574c66977fcee9d336e334ad1a3843a722be19123640e7808ea3")

    depends_on("py-google-api-core@1.34.0:3.0.0", type=("build", "run"))
    depends_on("py-proto-plus@1.2.2.0:2.0.0", type=("build", "run"))
    depends_on("py-protobuf@3.19.5:5.0.0", type=("build", "run"))
    depends_on("py-pandas@0.21.1:", type=("build", "run"))
    depends_on("py-fastavro@0.21.2:", type=("build", "run"))
    depends_on("py-pyarrow+parquet@0.15.0:", type=("build", "run"))
