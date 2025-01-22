# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyDiskcache(PythonPackage):
    """Disk Cache -- Disk and file backed persistent cache."""

    homepage = "http://www.grantjenks.com/docs/diskcache/"
    pypi = "diskcache/diskcache-4.1.0.tar.gz"

    license("Apache-2.0")

    version("5.6.3", sha256="2c3a3fa2743d8535d832ec61c2054a1641f41775aa7c556758a109941e33e4fc")
    version("5.6.1", sha256="e4c978532feff5814c4cc00fe1e11e40501985946643d73220d41ee7737c72c3")
    version("5.6.0", sha256="bc18c2a89e61672ea430a8bb908ede94eebcbb3a756d91403dd0e68f4755eb09")
    version("5.5.1", sha256="8685515584cc110a463d0728d98beaba56c7e2803b60a19cb8983a4c9e341d91")
    version("5.4.0", sha256="8879eb8c9b4a2509a5e633d2008634fb2b0b35c2b36192d89655dbde02419644")
    version("5.3.0", sha256="3f1fa30b29fdff26cfddcb3ee7d61376903f82c769ea2907a2b82a5bfb8abbe2")
    version("5.2.1", sha256="1805acd5868ac10ad547208951a1190a0ab7bbff4e70f9a07cde4dbdfaa69f64")
    version("5.2.1", sha256="1805acd5868ac10ad547208951a1190a0ab7bbff4e70f9a07cde4dbdfaa69f64")
    version("4.1.0", sha256="bcee5a59f9c264e2809e58d01be6569a3bbb1e36a1e0fb83f7ef9b2075f95ce0")

    depends_on("python", type=("build", "run"), when="@:4.1.0")
    depends_on("python@3:", type=("build", "run"), when="@5.2.1:")
    depends_on("py-setuptools", type="build")
