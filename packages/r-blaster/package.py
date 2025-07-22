# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlaster(RPackage):
	"""Native R Implementation of an Efficient BLAST-Like Algorithm

	Implementation of an efficient BLAST-like sequence
             comparison algorithm, written in 'C++11' and using
             native R datatypes. Blaster is based on 'nsearch' -
             Schmid et al (2018) <doi:10.1101/399782>.
	"""
	
	homepage = "https://github.com/tamminenlab/blaster"
	cran = "blaster" 

	version("1.0.7", sha256="6079eefe8afd2184eec81cc34fa8c8c34703a09ce35292cd6c730efb9b390ddc")
	version("1.0.6", sha256="04632503c43bafc21875069825b45da1f57ee2fc7f2cbc0b168701cb75400429")
	version("1.0.4", sha256="59c257c8303da8e505b05ba0b840d56020549c2fbef3e3367eb6075ff56c5b78")
	version("1.0.3", sha256="410d5900060914d2dbb821f798639a09a9ad20bfe49e5be5d08efef08b1c0032")
	version("1.0", sha256="a77599683cd2b4f6e77df4b12dc42a72731a7b6a3c9ef84e804b85655544f505")

	depends_on("r-rcpp", type=("build", "run"))
