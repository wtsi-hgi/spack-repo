# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyHaproh(PythonPackage):
    """Identify runs of homozygosity (hapROH) and contamination (hapCon) in ancient human DNA data."""

    homepage = "https://github.com/hringbauer/hapROH"
    pypi = "haproh/haproh-0.70.tar.gz"

    maintainers("softpack-bot")
    license("GPL-3.0-or-later")
    import_modules = ["hapsburg"]

    version("0.70", sha256="731b187de1e1c302d1fb606d9ce8f7cac495d9bfcd6a515fd34f175665622673")

    depends_on("py-setuptools", type="build")
    depends_on("py-cython", type="build")
    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-numdifftools", type=("build", "run"))

    def patch(self):
        filter_file(
            'license = "GPL-3.0-or-later"',
            'license = { text = "GPL-3.0-or-later" }',
            "pyproject.toml",
            string=True,
        )
        filter_file('license-files = ["LICENSE",]', "", "pyproject.toml", string=True)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            pyver = self.spec["python"].version.up_to(2)
            site_packages = join_path(self.prefix, f"lib/python{pyver}", "site-packages")
            env = os.environ.copy()
            env["PYTHONPATH"] = (
                f"{site_packages}{os.pathsep}{env['PYTHONPATH']}"
                if env.get("PYTHONPATH")
                else site_packages
            )
            python("-c", "import hapsburg", env=env)
