# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStakeholderanalysis(RPackage):
	"""Measuring Stakeholder Influence

	Proposes an original instrument for measuring stakeholder influence on the development of an infrastructure project that is carried through by a municipality, drawing on stakeholder classifications (Mitchell, Agle, & Wood, 1997) and input-output modelling (Hester & Adams, 2013). Mitchell R., Agle B.R., & Wood D.J. <doi:10.2307/259247> Hester, P.T., & Adams, K.M. (2013) <doi:10.1016/j.procs.2013.09.282>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "StakeholderAnalysis" 

	version("1.2", md5="6c81c3c985c3ac9fef405d90f7a91569")

	depends_on("r@3.2.3:", type=("build", "run"))
