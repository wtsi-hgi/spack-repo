# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPythonCinderclient(PythonPackage):
    """Client for the OpenStack Block Storage API."""

    homepage = "https://docs.openstack.org/python-cinderclient"
    pypi = "python-cinderclient/python_cinderclient-9.8.0.tar.gz"

    license("Apache-2.0")

    version("9.8.0", sha256="bd3ee9f9487c5e79957f018a6b3f2dece7059dad8f6155d83dd4b6eb9447a11d")

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-pbr@5.5.0:", type="build")
    depends_on("py-setuptools", type="build")

    depends_on("py-prettytable@0.7.2:", type=("build", "run"))
    depends_on("py-keystoneauth1@5.9.0:", type=("build", "run"))
    depends_on("py-oslo-i18n@5.0.1:", type=("build", "run"))
    depends_on("py-oslo-utils@4.8.0:", type=("build", "run"))
    depends_on("py-requests@2.25.1:", type=("build", "run"))
    depends_on("py-stevedore@3.3.0:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import cinderclient")
