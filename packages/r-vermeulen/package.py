# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVermeulen(RPackage):
	"""'Biomarker' Data Set by Vermeulen et al. (2009)

	The 'biomarker' data set by Vermeulen et al. (2009)
    <doi:10.1016/S1470-2045(09)70154-8> is provided. The data
    source, however, is by Ruijter et al. (2013)
    <doi:10.1016/j.ymeth.2012.08.011>. The original data set may
    be downloaded from
    <https://medischebiologie.nl/wp-content/uploads/2019/02/qpcrdatamethods.zip>.
    This data set is for a real-time quantitative polymerase chain reaction
    ('PCR') experiment that comprises the raw fluorescence data of 24,576
    amplification curves. This data set comprises 59 genes of interest and 5
    reference genes. Each gene was assessed on 366 neuroblastoma complementary
    DNA ('cDNA') samples and on 18 standard dilution series samples (10-fold
    5-point dilution series x 3 replicates + no template controls ('NTC') x 3
    replicates).
	"""
	
	homepage = "https://github.com/ramiromagno/vermeulen"
	cran = "vermeulen" 

	version("0.1.1", md5="ad4da4e29e76eda0adf9a09e1a16d430")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
