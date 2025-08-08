# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjson(RPackage):
    """JSON for R.

    Converts R object into JSON objects and vice-versa.
    """

    cran = "rjson"

    version("0.2.23", sha256="55034575c854ed657e6701da278c0fdea251479624d06a963b2e58461a5f0f48")
    version("0.2.22", sha256="06cdf67b72b6166a6ad399c8176b34f8a5a75fa5257ddbd46a2b99b2f39e1d27")

    depends_on("r@3.0:", type=("build", "run"))
