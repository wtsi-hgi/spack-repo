# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOscLib(PythonPackage):
    """OpenStackClient common library."""

    homepage = "https://docs.openstack.org/osc-lib/"
    # PyPI sdist is published with an underscore in the filename
    pypi = "osc-lib/osc_lib-4.2.0.tar.gz"

    license("Apache-2.0")

    version("4.2.0", sha256="99718f06a990c1ad6fb9034bbed9655390a2ea83cef71a53781e7e9abd9f20ce")

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-pbr@6.1.1:", type="build")
    depends_on("py-setuptools", type="build")

    depends_on("py-cliff@4.9.0:", type=("build", "run"))
    depends_on("py-keystoneauth1@5.10.0:", type=("build", "run"))
    depends_on("py-openstacksdk@0.15.0:", type=("build", "run"))
    depends_on("py-oslo-i18n@3.15.3:", type=("build", "run"))
    depends_on("py-oslo-utils@3.33.0:", type=("build", "run"))
    depends_on("py-requests@2.14.2:", type=("build", "run"))
    depends_on("py-stevedore@1.20.0:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import osc_lib")
