# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCampsis(RPackage):
	"""Generic PK/PD Simulation Platform CAMPSIS

	A generic, easy-to-use and intuitive
    pharmacokinetic/pharmacodynamic (PK/PD) simulation platform based on R
    packages 'rxode2', 'RxODE' and 'mrgsolve'. CAMPSIS provides an
    abstraction layer over the underlying processes of writing a PK/PD
    model, assembling a custom dataset and running a simulation. CAMPSIS
    has a strong dependency to the R package 'campsismod', which allows to
    read/write a model from/to files and adapt it further on the fly in
    the R environment. Package 'campsis' allows the user to assemble a
    dataset in an intuitive manner. Once the user’s dataset is ready, the
    package is in charge of preparing the simulation, calling 'rxode2',
    'RxODE' or 'mrgsolve' (at the user's choice) and returning the
    results, for the given model, dataset and desired simulation settings.
	"""
	
	homepage = "https://github.com/Calvagone/campsis"
	cran = "campsis" 

	version("1.5.1", md5="68a70753665b66b248096f8f55a38890")

	depends_on("r-campsismod@1.1:", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
