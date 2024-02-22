# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetplot(RPackage):
	"""Beautiful Graph Drawing

	A graph visualization engine that puts an emphasis on 
  aesthetics at the same time of providing default parameters that yield
  out-of-the-box-nice visualizations. The package is built on top of
  'The Grid Graphics Package' and seamlessly work with 'igraph' and 
  'network' objects.
	"""
	
	homepage = "https://github.com/USCCANA/netplot"
	cran = "netplot" 

	version("0.2-0", md5="ab9013b6073497493751b783b7587340")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
