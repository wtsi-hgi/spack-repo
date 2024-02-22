# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasydescribe(RPackage):
	"""A Convenient Way of Descriptive Statistics

	Descriptive Statistics is essential for publishing articles. This package can perform
    descriptive statistics according to different data types. If the data is a continuous variable,
    the mean and standard deviation or median and quartiles are automatically output; if the data
    is a categorical variable, the number and percentage are automatically output. In addition,
    if you enter two variables in this package, the two variables will be described and their
    relationships will be tested automatically according to their data types. For example,
    if one of the two input variables is a categorical variable, another variable will be described
    hierarchically based on the categorical variable and the statistical differences between
    different groups will be compared using appropriate statistical methods. And for groups of
    more than two, the post hoc test will be applied. For more information on the methods we used,
    please see the following references:
    Libiseller, C. and Grimvall, A. (2002) <doi:10.1002/env.507>,
    Patefield, W. M. (1981) <doi:10.2307/2346669>,
    Hope, A. C. A. (1968) <doi:10.1111/J.2517-6161.1968.TB00759.X>,
    Mehta, C. R. and Patel, N. R. (1983) <doi:10.1080/01621459.1983.10477989>,
    Mehta, C. R. and Patel, N. R. (1986) <doi:10.1145/6497.214326>,
    Clarkson, D. B., Fan, Y. and Joe, H. (1993) <doi:10.1145/168173.168412>,
    Cochran, W. G. (1954) <doi:10.2307/3001616>,
    Armitage, P. (1955) <doi:10.2307/3001775>,
    Szabo, A. (2016) <doi:10.1080/00031305.2017.1407823>,
    David, F. B. (1972) <doi:10.1080/01621459.1972.10481279>,
    Joanes, D. N. and Gill, C. A. (1998) <doi:10.1111/1467-9884.00122>,
    Dunn, O. J. (1964) <doi:10.1080/00401706.1964.10490181>,
    Copenhaver, M. D. and Holland, B. S. (1988) <doi:10.1080/00949658808811082>,
    Chambers, J. M., Freeny, A. and Heiberger, R. M. (1992) <doi:10.1201/9780203738535-5>,
    Shaffer, J. P. (1995) <doi:10.1146/annurev.ps.46.020195.003021>,
    Myles, H. and Douglas, A. W. (1973) <doi:10.2307/2063815>,
    Rahman, M. and Tiwari, R. (2012) <doi:10.4236/health.2012.410139>,
    Thode, H. J. (2002) <doi:10.1201/9780203910894>,
    Jonckheere, A. R. (1954) <doi:10.2307/2333011>,
    Terpstra, T. J. (1952) <doi:10.1016/S1385-7258(52)50043-X>.
	"""
	
	cran = "EasyDescribe" 

	version("0.1.2", md5="270e079dc6b8e76002d8134effd85942")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-multica", type=("build", "run"))
	depends_on("r-catt", type=("build", "run"))
	depends_on("r-gmodels", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-rcompanion", type=("build", "run"))
	depends_on("r-fsa", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-clinfun", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
