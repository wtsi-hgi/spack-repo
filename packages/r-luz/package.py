# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLuz(RPackage):
	"""Higher Level 'API' for 'torch'

	A high level interface for 'torch' providing utilities to reduce the
    the amount of code needed for common tasks, abstract away torch details and 
    make the same code work on both the 'CPU' and 'GPU'. It's flexible enough to
    support expressing a large range of models. It's heavily inspired by 'fastai' by 
    Howard et al. (2020) <arXiv:2002.04688>, 'Keras' by Chollet et al. (2015) and 
    'PyTorch Lightning' by Falcon et al. (2019) <doi:10.5281/zenodo.3828935>.
	"""
	
	homepage = "https://mlverse.github.io/luz/"
	cran = "luz" 

	version("0.4.0", md5="358a58e3d9c47dca171f8d28f25c4c62")

	depends_on("r-torch@0.9:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-zeallot", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-coro", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-prettyunits", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
