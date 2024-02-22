# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNsprcomp(RPackage):
	"""Non-Negative and Sparse PCA

	Two methods for performing a constrained principal
        component analysis (PCA), where non-negativity and/or sparsity
        constraints are enforced on the principal axes (PAs). The
        function 'nsprcomp' computes one principal component (PC) after
        the other. Each PA is optimized such that the corresponding PC
        has maximum additional variance not explained by the previous
        components. In contrast, the function 'nscumcomp' jointly
        computes all PCs such that the cumulative variance is maximal.
        Both functions have the same interface as the 'prcomp' function
        from the 'stats' package (plus some extra parameters), and both
        return the result of the analysis as an object of class
        'nsprcomp', which inherits from 'prcomp'. See
        <https://sigg-iten.ch/learningbits/2013/05/27/nsprcomp-is-on-cran/>
        and Sigg et al. (2008) <doi:10.1145/1390156.1390277> for more
        details.
	"""
	
	homepage = "https://sigg-iten.ch/research/"
	cran = "nsprcomp" 

	version("0.5.1-2", md5="2a10abde049fdcd04c30c1a4dc3409c3")

	depends_on("r@3.4:", type=("build", "run"))
