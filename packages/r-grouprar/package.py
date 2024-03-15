# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrouprar(RPackage):
	"""Group Response Adaptive Randomization for Clinical Trials

	
    Implement group response-adaptive randomization procedures, which also integrates standard non-group response-adaptive randomization methods as specialized instances. It is also uniquely capable of managing complex scenarios, including those with delayed and missing responses, thereby expanding its utility in real-world applications. This package offers 16 functions for simulating a variety of response adaptive randomization procedures. These functions are essential for guiding the selection of statistical methods in clinical trials, providing a flexible and effective approach to trial design. Some of the detailed methodologies and algorithms used in this package, please refer to the following references:
    LJ Wei (1979) <doi:10.1214/aos/1176344614>
    L. J. WEI and S. DURHAM (1978) <doi:10.1080/01621459.1978.10480109>
    Durham, S. D., FlournoY, N. AND LI, W. (1998) <doi:10.2307/3315771>
    Ivanova, A., Rosenberger, W. F., Durham, S. D. and Flournoy, N. (2000) <https://www.jstor.org/stable/25053121>
    Bai Z D, Hu F, Shen L. (2002) <doi:10.1006/jmva.2001.1987>
    Ivanova, A. (2003) <doi:10.1007/s001840200220>
    Hu, F., & Zhang, L. X. (2004) <doi:10.1214/aos/1079120137>
    Hu, F., & Rosenberger, W. F. (2006, ISBN:978-0-471-65396-7).
    Zhang, L. X., Chan, W. S., Cheung, S. H., & Hu, F. (2007) <https://www.jstor.org/stable/26432528>
    Zhang, L., & Rosenberger, W. F. (2006) <doi:10.1111/j.1541-0420.2005.00496.x>
    Hu, F., Zhang, L. X., Cheung, S. H., & Chan, W. S. (2008) <doi:10.1002/cjs.5550360404>.
	"""
	
	cran = "grouprar" 

	version("0.1.0", md5="c86abfa938243d372035decb2cfeaa37")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
