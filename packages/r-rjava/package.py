# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjava(RPackage):
	"""Low-Level R to Java Interface.

	Low-level interface to Java VM very much like .C/.Call and friends.  Allows
	creation of objects, calling methods and accessing fields."""

	cran = "rJava"
	version("1.0-6", sha256="e290d0493317a5d6c452793e92baa914e37ef03faef19b2e436329b4ec8658c6")
	version("0.9-13", sha256="5b1688f5044476b34f71d868b222ac5fce3a088f0c2b9e4591c1e48f3d8c75f4")
	version("0.9-11", sha256="c28ae131456a98f4d3498aa8f6eac9d4df48727008dacff1aa561fc883972c69")
	version("0.9-8", sha256="dada5e031414da54eb80b9024d51866c20b92d41d68da65789fe0130bc54bd8a")
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
