# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRequestsexceptions(PythonPackage):
    """Import exceptions from bundled dependencies inside requests."""

    homepage = "https://opendev.org/openstack/requestsexceptions"
    pypi = "requestsexceptions/requestsexceptions-1.4.0.tar.gz"

    license("Apache-2.0")

    version("1.4.0", sha256="b095cbc77618f066d459a02b137b020c37da9f46d9b057704019c9f77dba3065")

    depends_on("python@3.8:", type=("build", "run"))

    depends_on("py-setuptools", type="build")
    depends_on("py-pbr@2.0.0:", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import requestsexceptions")
