# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RAll(RPackage):
    """Data of T- and B-cell Acute Lymphocytic Leukemia from the Ritz Laboratory at the DFCI (includes Apr 2004 versions)."""

    url = "https://bioconductor.org/packages/release/data/experiment/src/contrib/ALL_1.44.0.tar.gz"
    bioc = "ALL"

    version("1.44.0", sha256="6c52471acf4bb77ed86e71c25e69ce5cc5235acec50785107b212934c6eec5db")

    depends_on("r@2.1.0:", type=("build", "run"))
    depends_on("r-biobase@2.5.5:", type=("build", "run"))
