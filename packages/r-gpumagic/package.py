# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpumagic(RPackage):
	"""An openCL compiler with the capacity to compile R functions and run the code on GPU

	The package aims to help users write openCL code with little or no effort. It is able to compile an user-defined R function and run it on a device such as a CPU or a GPU. The user can also write and run their openCL code directly by calling .kernel function.
	"""
	
	bioc = "gpuMagic" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/gpuMagic_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/gpuMagic/gpuMagic_1.18.0.tar.gz"]

	version("1.18.0", md5="b720e953b36ccc2db0c6b359f84b5c94")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("ocl-icd", type=("build", "link", "run"))
