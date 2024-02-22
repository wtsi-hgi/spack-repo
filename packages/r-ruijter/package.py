# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRuijter(RPackage):
	"""Technical Data Sets by 'Ruijter et al.' (2013)

	The real-time quantitative polymerase chain reaction
    ('PCR') technical data sets by 'Ruijter et al.' (2013)
    <doi:10.1016/j.ymeth.2012.08.011>: (i) the four-point 10-fold dilution
    series; (ii) 380 replicates; and (iii) the 'competimer' data set. These
    three data sets can be used to benchmark 'qPCR' methods. Original data set
    is available at
    <https://medischebiologie.nl/wp-content/uploads/2019/02/qpcrdatamethods.zip>.
    This package fixes incorrect annotations in the original data sets.
	"""
	
	homepage = "https://github.com/ramiromagno/ruijter"
	cran = "ruijter" 

	version("0.1.2", md5="24ba5f23563618e30789f8b292e90486")

	depends_on("r@2.10:", type=("build", "run"))
