# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQcapower(RPackage):
	"""Estimate Power and Required Sample Size in QCA

	Researchers working with Qualitative Comparative Analysis (QCA)
    can use the package to estimate power of a sufficient term
    using permutation tests. A term can be anything: A condition, conjunction or 
    disjunction of any combination of these. The package further allows users to plot 
    the estimation results and to estimate the number of cases required to achieve a
    certain level of power, given a prespecified null and alternative hypothesis.
    Reference for the article introducing power estimation for QCA is: 
    Rohlfing, Ingo (2018) <doi:10.1017/pan.2017.30> 
    (ungated version: <doi:10.17605/OSF.IO/PC4DF>).
	"""
	
	homepage = "https://github.com/ingorohlfing/qcapower"
	cran = "qcapower" 

	version("0.1.0", md5="d8b8f2af7bf59db47b15a78c145f0635")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
