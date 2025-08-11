# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMetroapi(PythonPackage):
    # Metro: A batteries-included web framework for the fastest development experience.
    homepage = "https://github.com/ricardo-agz/metro"
    pypi = "metroapi/metroapi-0.0.12.tar.gz"
    import_modules = ["metro"]

    # Variants for extras
    variant("conductor", default=False, description="Enable conductor extra")


    version("0.0.12", sha256="57154699b9578c5683f17917ce8bd08dfd5fbf27f6c325bbe181ca7fad77e6fb")

    # Rely on uv to manage and install all dependencies from PyPI
    depends_on("py-uv", type=("build", "run"))

    def install(self, spec, prefix):
        extras = []
        if "+conductor" in spec:
            extras.append("conductor")
        extras_suffix = f"[{','.join(extras)}]" if extras else ""
        pkg_spec = f"metroapi{extras_suffix}=={self.version}"
        python("-m", "uv", "pip", "install", pkg_spec, f"--prefix={prefix}")


    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", 'import metro')