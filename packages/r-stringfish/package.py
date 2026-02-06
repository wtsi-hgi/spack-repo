# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStringfish(RPackage):
	"""Alt String Implementation.

	Provides an extendable, performant and multithreaded 'alt-string'
	implementation backed by 'C++' vectors and strings."""

	cran = "stringfish"

	maintainers("dorton21")
	version("0.18.0", sha256="e2df642db65b03e15e7762d7fa612bb84f7bf6b20007ceab2bfe3b93f1163aef")
	version("0.17.0", sha256="9e0af5404b07c2db5912f8663dbb6f09c813b5598d7ec90fd5501f1c4453d674")
	version("0.16.0", sha256="3608bc83900246297b38df46954bd9aa3b6f463a56eefbe80cfc713eab797993")
	version("0.15.8", sha256="dfb21e2941b1884f5ee1f2d286b986bb4b7f607eb68edc3f0c5a7079da88839b")
	version("0.15.7", sha256="34b1703a8876a40860d35f88a94e069832a7d2bc86189ff07af84ff04fd4b735")
	version("0.15.5", sha256="9df21146a7710e5a9ab4bb53ebc231a580c798b7e541b8d78df53207283f8129")
	version("0.15.4", sha256="8e0f94e7a5afd6d120f84ec0ad446554ada74be5a185041a466ba3fd76f2c7d8")
	version("0.15.3", sha256="8f5187b90995fa3ce3b3a7c27820a476bccab39548aee980e1045e36da71990c")
	version("0.15.2", sha256="f60e602155a6ef4efbd57d9dda3bda91f01e3f1ad9dbf28415bfac176e410455")
	version("0.15.1", sha256="e38ab62505145c5141317463cc6784ef619fad2e82ca0c4322616415f281c404")
	version("0.15.0", sha256="9984fad738530601622f38ad84bbbf62820f83d1d8153fdd163e8e4fc1c1fab7")
	version("0.14.2", sha256="9373cfc715cda1527fd20179435977b8e59e19d8c5ef82a31e519f93fb624ced")
	version("0.14.1", sha256="ec69704c6984e67f7f24e38a8aad5f4283bb85aacd3325bc57300ee95fe105b9")
	version("0.13.3", sha256="152d206c19de086bad560698557a984283d7b962fbf44598e88e64ae7b690ca7")
	version("0.13.2", sha256="c22b2147e21b38fa9fcf73c21d040c69fe59e23701eddf8f58962aa9c0e7e11b")
	version("0.12.1", sha256="39e8b57211ba816f1453d438af797dda0ffc2ed8c087569e9b51e052d3d704e0")
	version("0.12", sha256="4e04f56898b4cffee09bd5a90e1e7470bed9a15205bc5edcb76243254b8c60dd")
	version("0.11", sha256="cbb5ff86935da649472a1ecfc7979d5a9c698959e66a940e224e77247b07ab39")

	depends_on("r@3.6.0:", when="@0.17.0:")
	depends_on("r@3.0.2:", type=("build", "run"), when="@:0.17.0")
	depends_on("r-rcpp@0.12.18.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.1.4:", type=("build", "run"))
