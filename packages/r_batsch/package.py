# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBatsch(RPackage):
	"""Real-Time PCR Data Sets by Batsch et al. (2008)

	Real-time quantitative polymerase chain reaction (qPCR) data
    sets by Batsch et al. (2008) <doi:10.1186/1471-2105-9-95>. This package
    provides five data sets, one for each PCR target: (i) rat SLC6A14,
    (ii) human SLC22A13, (iii) pig EMT, (iv) chicken ETT, and (v) human
    GAPDH. Each data set comprises a five-point, four-fold dilution series.
    For each concentration there are three replicates. Each amplification curve
    is 45 cycles long. Original raw data file:
    <https://static-content.springer.com/esm/art%3A10.1186%2F1471-2105-9-95/MediaObjects/12859_2007_2080_MOESM5_ESM.xls>.
	"""
	
	homepage = "https://github.com/ramiromagno/batsch"
	cran = "batsch" 

	version("0.1.0", md5="1ab2fde7d0c3c4b9110cf9d35ab8edad")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
