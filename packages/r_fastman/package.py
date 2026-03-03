# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastman(RPackage):
    """An R package for fast and efficient visualizing of GWAS results using Q-Q and Manhattan plots directly from PLINK output files."""

    homepage = "https://github.com/kaustubhad/fastman"
    git = "https://github.com/kaustubhad/fastman.git"

    version("2023-02-10", commit="365b9f50d868b0dde9061bb7f7af8a9f4232ec60")

    # depends_on("r-", type=("build", "run"))
