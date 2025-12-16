# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyKeystoneauth1(PythonPackage):
    """
    This package contains tools for authenticating to an OpenStack-based
    cloud
    """

    homepage = "https://docs.openstack.org/keystoneauth/"
    pypi = "keystoneauth1/keystoneauth1-4.3.1.tar.gz"

    maintainers("haampie")

    version("5.10.0", sha256="34b870dbbcf806cdb5aec98483b62820a6568d364eca7b1174ca6a8b5a9c77ed")
    version("4.3.1", sha256="93605430a6d1424f31659bc5685e9dc1be9a6254e88c99f00cffc0a60c648a64")

    depends_on("python@3.6:", when="@:4", type=("build", "run"))
    depends_on("python@3.8:", when="@5:", type=("build", "run"))

    depends_on("py-pbr@2.0.0:2.0,2.1.1:", type="build")
    depends_on("py-setuptools", type="build")

    depends_on("py-iso8601@0.1.11:", when="@:4", type=("build", "run"))
    depends_on("py-iso8601@2.0.0:", when="@5:", type=("build", "run"))
    depends_on("py-requests@2.14.2:", type=("build", "run"))
    depends_on("py-six@1.10.0:", type=("build", "run"))
    depends_on("py-stevedore@1.20.0:", type=("build", "run"))
    depends_on("py-os-service-types@1.2.0:", type=("build", "run"))
    depends_on("py-typing-extensions@4.12:", when="@5:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import keystoneauth1")
