# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOsServiceTypes(PythonPackage):
    """Python library for consuming OpenStack sevice-types-authority data"""

    homepage = "https://docs.openstack.org/os-service-types/"
    pypi = "os-service-types/os_service_types-1.8.2.tar.gz"

    maintainers("haampie")

    version("1.8.2", sha256="ab7648d7232849943196e1bb00a30e2e25e600fa3b57bb241d15b7f521b5b575")
    version("1.7.0", sha256="31800299a82239363995b91f1ebf9106ac7758542a1e4ef6dc737a5932878c6c")

    depends_on("python@2.7:2.8,3.5:", when="@:1.7", type=("build", "run"))
    depends_on("python@3.10:", when="@1.8:", type=("build", "run"))
    depends_on("py-pbr@2.0.0:", type="build")
    depends_on("py-setuptools", type="build")
    # os_service_types/types.py imports typing_extensions at runtime
    depends_on("py-typing-extensions", when="@1.8:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import os_service_types")
