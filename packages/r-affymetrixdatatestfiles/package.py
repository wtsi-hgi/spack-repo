# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffymetrixdatatestfiles(RPackage):
    """Affymetrix Data Files (CEL, CDF, CHP, EXP, PGF, PSI) for Testing

    This package contains annotation data files and sample data files of Affymetrix file formats.  The files originate from the Affymetrix' Fusion SDK distribution and other official sources.
    """

    bioc = "AffymetrixDataTestFiles"

    version("0.46.0", commit="dbafce59ab58dc1bdeed5d8fd429a76227bd90d8")
    version("0.40.0", commit="6b95627c6fbcb199750d32ee94c78b063e552520")

    depends_on("r@2.5:", type=("build", "run"))
