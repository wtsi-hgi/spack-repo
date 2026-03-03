# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOpenstacksdk(PythonPackage):
    """SDK for building applications against OpenStack."""

    homepage = "https://docs.openstack.org/openstacksdk"
    pypi = "openstacksdk/openstacksdk-4.8.0.tar.gz"

    license("Apache-2.0")

    version("4.8.0", sha256="4dc038e1c17d893005f3a0a8951456afd9d148f3f65d448f94adcceb278d7f31")

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-pbr@6.1.1:", type="build")
    depends_on("py-setuptools", type="build")

    depends_on("py-cryptography@2.7:", type=("build", "run"))
    depends_on("py-decorator@4.4.1:", type=("build", "run"))
    depends_on("py-dogpile-cache@0.6.5:", type=("build", "run"))
    depends_on("py-iso8601@0.1.11:", type=("build", "run"))
    depends_on("py-jmespath@0.9.0:", type=("build", "run"))
    depends_on("py-jsonpatch@1.16:", type=("build", "run"))
    depends_on("py-keystoneauth1@5.10.0:", type=("build", "run"))
    depends_on("py-os-service-types@1.8.0:", type=("build", "run"))
    depends_on("py-platformdirs@3:", type=("build", "run"))
    depends_on("py-psutil@3.2.2:", type=("build", "run"))
    depends_on("py-pyyaml@3.13:", type=("build", "run"))
    depends_on("py-requestsexceptions@1.2.0:", type=("build", "run"))
    depends_on("py-typing-extensions@4.12:", type=("build", "run"))

    conflicts("^py-jsonpatch@1.20", msg="openstacksdk requires jsonpatch!=1.20")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import openstack")
