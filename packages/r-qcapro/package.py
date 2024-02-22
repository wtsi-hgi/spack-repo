# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQcapro(RPackage):
	"""Advanced Functionality for Performing and Evaluating Qualitative
Comparative Analysis

	Provides advanced functionality for performing configurational comparative research with Qualitative Comparative Analysis (QCA), including crisp-set, multi-value, and fuzzy-set QCA. It also offers advanced tools for sensitivity diagnostics and methodological evaluations of QCA.
	"""
	
	homepage = "http://www.alrik-thiem.net/;"
	cran = "QCApro" 

	version("1.1-2", md5="f090988d12c3a6171b4df58dd2bcaf3f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
