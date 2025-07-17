# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScanUpc(RPackage):
    """Single-channel array normalization (SCAN) and Universal exPression Codes (UPC)

    SCAN is a microarray normalization method to facilitate personalized-medicine workflows. Rather than processing microarray samples as groups, which can introduce biases and present logistical challenges, SCAN normalizes each sample individually by modeling and removing probe- and array-specific background noise using only data from within each array. SCAN can be applied to one-channel (e.g., Affymetrix) or two-channel (e.g., Agilent) microarrays. The Universal exPression Codes (UPC) method is an extension of SCAN that estimates whether a given gene/transcript is active above background levels in a given sample. The UPC method can be applied to one-channel or two-channel microarrays as well as to RNA-Seq read counts. Because UPC values are represented on the same scale and have an identical interpretation for each platform, they can be used for cross-platform data integration.
    """

    homepage = "http://bioconductor.org"
    bioc = "SCAN.UPC"

    version("2.50.0", commit="ad3cd0f3d1788e089291e15aeaae0b8488e826b0")
    version("2.44.0", commit="2687df9cb3073e7cbb939e6b84c5a05c557e34e7")

    depends_on("r@2.14:", type=("build", "run"))
    depends_on("r-biobase@2.6:", type=("build", "run"))
    depends_on("r-oligo", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-geoquery", type=("build", "run"))
    depends_on("r-affy", type=("build", "run"))
    depends_on("r-affyio", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-sva", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
