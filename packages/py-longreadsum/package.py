# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack.package import *


class PyLongreadsum(PythonPackage):
    """LongReadSum: A fast and flexible QC tool for long read sequencing data.
    
    LongReadSum supports FASTA, FASTQ, BAM, FAST5, and sequencing_summary.txt 
    file formats for quick generation of QC data in HTML and text format."""

    homepage = "https://github.com/WGLab/LongReadSum"
    url = "https://github.com/WGLab/LongReadSum/archive/refs/tags/v1.5.0.tar.gz"

    maintainers("WGLab")

    license("MIT")

    version("1.5.0", sha256="fe3acc37bdd5e703033b9e370f635ab9fe06ba09fd69e01fc00bc70ff6d8395a")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-plotly", type=("build", "run"))
    depends_on("py-pyarrow", type=("build", "run"))
    # ONT POD5 and VBZ plugin support (pure Python wheels)
    depends_on("py-pod5", type=("build", "run"))
    depends_on("py-vbz-h5py-plugin", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("py-pytest", type="test")
    
    # htslib provides <htslib/sam.h> and libhts used by the C++ extension
    depends_on("htslib@1.20:", type=("build", "link", "run"))
    # HDF5 C++ and High-level APIs are required for headers like H5Cpp.h and libs
    depends_on("hdf5+cxx+hl", type=("build", "link", "run"))
    # Build SWIG wrapper for the Python extension
    depends_on("swig", type="build")

    def patch(self):
        # Upstream hardcodes script_args in setup(), which breaks pip's egg_info
        # phase under Spack. Remove it so pip can drive build/install properly.
        filter_file("script_args=['build_ext', '--build-lib', 'lib'],", "", "setup.py", string=True)
        # Fix console entrypoint to point at installed package path
        filter_file("longreadsum.__main__:main", "src.cli:main", "setup.py", string=True)
        # Ensure SWIG interface is compiled as part of the extension
        filter_file(
            "sources=project_src_files,",
            "sources=['src/lrst.i'] + project_src_files, swig_opts=['-c++', '-py3', '-Iinclude'],",
            "setup.py",
            string=True,
        )
        # Use installed import path for lrst in CLI
        filter_file("from lib import lrst", "import lrst", "src/cli.py", string=True)

    @run_after('install')
    def add_lrst_shims(self):
        # Provide shim modules so imports work in both dev and installed modes
        import glob
        site_roots = glob.glob(os.path.join(self.prefix, 'lib', 'python*', 'site-packages'))
        if not site_roots:
            return
        site_root = site_roots[0]

        # Top-level lrst shim -> exposes symbols from _lrst
        lrst_py = os.path.join(site_root, 'lrst.py')
        if not os.path.exists(lrst_py):
            with open(lrst_py, 'w') as f:
                f.write('from _lrst import *\n')

        # lib/lrst shim for src.cli debug import path
        lib_dir = os.path.join(site_root, 'lib')
        os.makedirs(lib_dir, exist_ok=True)
        init_py = os.path.join(lib_dir, '__init__.py')
        if not os.path.exists(init_py):
            with open(init_py, 'w') as f:
                f.write('')
        lib_lrst_py = os.path.join(lib_dir, 'lrst.py')
        if not os.path.exists(lib_lrst_py):
            with open(lib_lrst_py, 'w') as f:
                f.write('from _lrst import *\n')

    def setup_build_environment(self, env):
        hts = self.spec["htslib"]
        hdf5 = self.spec["hdf5"]
        # Common convention used by projects to locate external htslib
        env.set("HTSLIB_MODE", "external")
        env.set("HTSLIB_INCLUDE_DIR", hts.headers.directories[0])
        env.set("HTSLIB_LIBRARY_DIR", hts.libs.directories[0])

        # Ensure compiler and linker can find headers and libraries
        env.append_flags("CPPFLAGS", hts.headers.cpp_flags)
        env.append_flags("CPPFLAGS", hdf5.headers.cpp_flags)
        env.append_flags("LDFLAGS", hts.libs.search_flags)
        env.append_flags("LDFLAGS", hdf5.libs.search_flags)

        # Some build systems respect HDF5_DIR explicitly
        env.set("HDF5_DIR", str(hdf5.prefix))
    
