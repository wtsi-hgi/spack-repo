# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsigdbr(RPackage):
	"""MSigDB Gene Sets for Multiple Organisms in a Tidy Data Format

	Provides the 'Molecular Signatures Database' (MSigDB) gene
    sets typically used with the 'Gene Set Enrichment Analysis' (GSEA)
    software (Subramanian et al. 2005 <doi:10.1073/pnas.0506580102>,
    Liberzon et al. 2015 <doi:10.1016/j.cels.2015.12.004>) in a standard R
    data frame with key-value pairs. The package includes the human genes
    as listed in MSigDB as well as the corresponding symbols and IDs for
    frequently studied model organisms such as mouse, rat, pig, fly, and
    yeast.
	"""
	
	homepage = "https://igordot.github.io/msigdbr/"
	cran = "msigdbr" 

	version("7.5.1", md5="3c4b7f8546f159363d4f95c9d170f09b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-babelgene", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
