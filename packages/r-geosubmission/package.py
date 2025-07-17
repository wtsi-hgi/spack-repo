# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeosubmission(RPackage):
    """Prepares microarray data for submission to GEO

    Helps to easily submit a microarray dataset and the associated sample information to GEO by preparing a single file for upload (direct deposit).
    """

    bioc = "GEOsubmission"

    version("1.60.0", commit="aa7e9e2ea5a180402e42bec596dba1f8d37d2176")
    version("1.54.0", commit="29171b7b3bb7bcee73ad8f2025be49aef35a0983")

    depends_on("r-affy", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
