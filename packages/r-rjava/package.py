# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjava(RPackage):
	"""Low-Level R to Java Interface.

	Low-level interface to Java VM very much like .C/.Call and friends.  Allows
	creation of objects, calling methods and accessing fields."""

	cran = "rJava"

	version("1.0-11", md5="4d8eff03a23cb797f01e710ea7528dd2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("openjdk@1.2:", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
	depends_on("icu4c", type=("build", "link", "run"))
	depends_on("libiconv", type=("build", "link", "run"))

	def setup_build_environment(self, env):
		spec = self.spec
		env.append_flags("JAVAH", "{0}/javah".format(join_path(spec["java"].prefix.bin)))
