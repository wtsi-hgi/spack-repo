# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydataGoogleAuth(PythonPackage):
    """pydata-google-auth is a package providing helpers for authenticating to Google APIs."""

    homepage = "https://github.com/pydata/pydata-google-auth"
    pypi = "pydata-google-auth/pydata-google-auth-1.8.2.tar.gz"

    version("1.8.2", sha256="547b6c0fbea657dcecd50887c5db8640ebec062a59a2b88e8ff8e53a04818303")

    depends_on("py-google-auth@1.25.0:", type=("build", "run"))
    depends_on("py-google-auth-oauthlib@0.4.0:", type=("build", "run"))
