# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RIrkernel(RPackage):
	"""Native R Kernel for the 'Jupyter Notebook'.

	The R kernel for the 'Jupyter' environment executes R code which the
	front-end ('Jupyter Notebook' or other front-ends) submits to the kernel
	via the network."""

	cran = "IRkernel"

	version("1.3.2", md5="491232d151d5b61ed29d5fd0c6ef7b8a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-repr@0.4.99:", type=("build", "run"))
	depends_on("r-evaluate@0.10:", type=("build", "run"))
	depends_on("r-irdisplay@0.3.0.9999:", type=("build", "run"))
	depends_on("r-pbdzmq@0.2.1:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-jsonlite@0.9.6:", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("py-jupyter", type=("build", "link", "run"))
