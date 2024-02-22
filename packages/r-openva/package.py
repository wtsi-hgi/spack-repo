# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenva(RPackage):
	"""Automated Method for Verbal Autopsy

	Implements multiple existing open-source algorithms for coding cause of death from verbal autopsies. The methods implemented include 'InterVA4' by Byass et al (2012) <doi:10.3402/gha.v5i0.19281>, 'InterVA5' by Byass at al (2019) <doi:10.1186/s12916-019-1333-6>, 'InSilicoVA' by McCormick et al (2016) <doi:10.1080/01621459.2016.1152191>, 'NBC' by Miasnikof et al (2015) <doi:10.1186/s12916-015-0521-2>, and a replication of 'Tariff' method by James et al (2011) <doi:10.1186/1478-7954-9-31> and Serina, et al. (2015) <doi:10.1186/s12916-015-0527-9>. It also provides tools for data manipulation tasks commonly used in Verbal Autopsy analysis and implements easy graphical visualization of individual and population level statistics. The 'NBC' method is implemented by the 'nbc4va' package that can be installed from <https://github.com/rrwen/nbc4va>. Note that this package was not developed by authors affiliated with the Institute for Health Metrics and Evaluation and thus unintentional discrepancies may exist in the implementation of the 'Tariff' method.
	"""
	
	homepage = "https://github.com/verbal-autopsy-software/openVA"
	cran = "openVA" 

	version("1.1.2", md5="e9504b713bf0c055a5dc4bf2fa29f9ac")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-interva5@1.0.1:", type=("build", "run"))
	depends_on("r-insilicova@1.1.3:", type=("build", "run"))
	depends_on("r-interva4@1.7.3:", type=("build", "run"))
	depends_on("r-tariff@1.0.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
