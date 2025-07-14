# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHicexperiment(RPackage):
	"""Bioconductor class for interacting with Hi-C files in R

	R generic interface to Hi-C contact matrices in `.(m)cool`, `.hic` or HiC-Pro derived formats, as well as other Hi-C processed file formats. Contact matrices can be partially parsed using a random access method, allowing a memory-efficient representation of Hi-C data in R. The `HiCExperiment` class stores the Hi-C contacts parsed from local contact matrix files. `HiCExperiment` instances can be further investigated in R using the `HiContacts` analysis package.
	"""
	
	homepage = "https://github.com/js2264/HiCExperiment"
	bioc = "HiCExperiment"

	version("1.8.0", commit="d884cd3ce859e4e185cf72aa1fe5b58b9211304a")
	version("1.2.0", commit="ee18f17762a1fdb8ea57a18ff20f2387c33e8f5f")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-interactionset", type=("build", "run"))
	depends_on("r-strawr", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocio", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
