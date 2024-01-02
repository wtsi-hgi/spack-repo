# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPandasGbq(PythonPackage):
    """pandas-gbq is a package providing an interface to the Google BigQuery API from pandas."""

    homepage = "https://github.com/googleapis/python-bigquery-pandas"
    pypi = "pandas-gbq/pandas-gbq-0.19.2.tar.gz"

    version("0.19.2", sha256="b0f7fa84a2be0fe767e33a008ca7e4ad9a9e3ac67255fd0a41fc19b503138447")

    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-google-auth", type=("build", "run"))
    depends_on("py-google-auth-oauthlib", type=("build", "run"))
    depends_on("py-google-cloud-bigquery", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
