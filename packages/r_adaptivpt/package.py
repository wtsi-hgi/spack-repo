# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdaptivpt(RPackage):
	"""Adaptive Bioequivalence Design for In-Vitro Permeation Tests

	Contains functions carrying out adaptive procedures using mixed scaling approach to establish bioequivalence for in-vitro permeation test (IVPT) data. Currently, the package provides procedures based on parallel replicate design and balanced data, according to the U.S. Food and Drug Administration's "Draft Guidance on Acyclovir" <https://www.accessdata.fda.gov/drugsatfda_docs/psg/Acyclovir_topical%20cream_RLD%2021478_RV12-16.pdf>. Potvin et al. (2008) <doi:10.1002/pst.294> provides the basis for our adaptive design (see Method B). For a comprehensive overview of the method, refer to Lim et al. (2023) <doi:10.1002/pst.2333>. This package reflects the views of the authors and should not be construed to represent the views or policies of the U.S. Food and Drug Administration.
	"""
	
	cran = "adaptIVPT" 

	version("1.1.0", md5="c5a6125b43ae3b6c88331ffc32646653")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
