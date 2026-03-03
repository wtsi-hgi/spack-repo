# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpyants(RPackage):
	"""An Alternative Advanced Normalization Tools ('ANTs')

	
    Provides portable access from 'R' to biomedical image processing toolbox 
    'ANTs' by Avants et al. (2009) <doi:10.54294/uvnhin> via seamless
    integration with the 'Python' implementation 'ANTsPy'. Allows biomedical 
    images to be processed in 'Python' and analyzed in 'R', and vice versa 
    via shared memory. See 'citation("rpyANTs")' for more reference information.
	"""
	
	homepage = "http://dipterix.org/rpyANTs/"
	cran = "rpyANTs" 

	version("0.0.3", md5="bd2cd21d78303cb2564625570403922e")

	depends_on("r-rpymat@0.1.6:", type=("build", "run"))
	depends_on("r-reticulate@1.26:", type=("build", "run"))
	depends_on("r-rnifti@1.5:", type=("build", "run"))
