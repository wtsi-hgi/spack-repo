# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os
import shutil
import subprocess
import spack.filesystem_view as sview


class PyCadqueryOcp(PythonPackage):
    """Python wrapper for Open CASCADE Technology 3D geometry library based on the official CadQuery/OCP sources"""
    
    homepage = "https://github.com/CadQuery/OCP"
    pypi = "cadquery-ocp/cadquery_ocp-7.8.1.1.post1-cp313-cp313-manylinux_2_31_x86_64.whl" 

    version("7.5.3.0-py310", sha256="63f265f79999094869a131e642e8494519a6c4fbb927472a0d46a142064a39f2", expand=False, url="https://files.pythonhosted.org/packages/a0/ed/8b885e4e79ac7fcd8cd6fce743cbc1f1f24a5a29a167cb4e9fe3cbd95c97/cadquery_ocp-7.5.3-cp310-cp310-manylinux_2_31_x86_64.whl")
    version("7.5.3.0-py38", sha256="16962b0b625fc32d21d3b8472dce7ea72a4ee53928f85d127ac3772f688456bf", expand=False, url="https://files.pythonhosted.org/packages/66/a8/6a6cfa53f24761d9c84f04abb14b8d8a375a980e4b149780461389fe9d77/cadquery_ocp-7.5.3-cp38-cp38-manylinux_2_31_x86_64.whl")
    version("7.5.3.0-py39", sha256="982f0349c8258bfb10a39d71e80de1c7f1589822f7129d619cd4cd3423e5df01", expand=False, url="https://files.pythonhosted.org/packages/8b/42/d2af73a86b6107acaf72fe02dfa02f5d53fa50257f5e68a27d2ab1637de2/cadquery_ocp-7.5.3-cp39-cp39-manylinux_2_31_x86_64.whl")
    version("7.6.3-py310", sha256="d8cbd440557914458e103230728449c0477521496e9cd4bd18f662e5fa671f31", expand=False, url="https://files.pythonhosted.org/packages/80/01/c9781a88b601ffabd88c1fd8f587beaaabaff0390fcc718f667e07ff234f/cadquery_ocp-7.6.3-cp310-cp310-manylinux_2_31_x86_64.whl")
    version("7.6.3-py38", sha256="751222bd50b2884ec8ddd3ac4113647e6679f4bca9c76d208bd02a7fdcf2b523", expand=False, url="https://files.pythonhosted.org/packages/46/16/bec3ded213b335ce3572835aed7b3235d768c6383e0ca057f2e579a3f49b/cadquery_ocp-7.6.3-cp38-cp38-manylinux_2_31_x86_64.whl")
    version("7.6.3-py39", sha256="2cf5e851f43895b51022c5689c08eb5e02a08e68fcd5ea9c7503279848cc87d6", expand=False, url="https://files.pythonhosted.org/packages/ac/7f/4b062d337c430c1991261acfbd8931200f56c157ae2aca747b455e955cd8/cadquery_ocp-7.6.3-cp39-cp39-manylinux_2_31_x86_64.whl")
    version("7.6.3a0-py310", sha256="74a87e0a98b2d4ce3ac77408a90ca4ef4f63589a7d4d2291c9d3a80df6c5410e", expand=False, url="https://files.pythonhosted.org/packages/5e/b2/4d19b727574a9d17450c5b1902ef440eb57ad6c0df37f7ab65a8f982f28f/cadquery_ocp-7.6.3a0-cp310-cp310-manylinux_2_31_x86_64.whl")
    version("7.6.3a0-py38", sha256="56dfda2dc5cbfa6fa23fd4296f21332b782cc25eb84a6b05b5b5512b243418d3", expand=False, url="https://files.pythonhosted.org/packages/22/a6/a55e7efd04f9974bc080a7c42ee4cf6cabfa6d91c1f5fde6643cb5c2ef5d/cadquery_ocp-7.6.3a0-cp38-cp38-manylinux_2_31_x86_64.whl")
    version("7.6.3a0-py39", sha256="ca1192e6a8d38a5206d2f8c2c6a4e13331cca90f70725d110460c050c82af0f6", expand=False, url="https://files.pythonhosted.org/packages/4f/30/871bce7460b907129e7dacbce4998c074124402582ddb1cc9fd1badb5783/cadquery_ocp-7.6.3a0-cp39-cp39-manylinux_2_31_x86_64.whl")
    version("7.7.0-py310", sha256="6c54559120da913ad3e4d0d0de3695d373db4de2288389b11e2fe9add8004048", expand=False, url="https://files.pythonhosted.org/packages/7f/1d/9cc4e8917bf0ebd8993ccbc15e9c84d024d4f546a8fb883595e1d20170ae/cadquery_ocp-7.7.0-cp310-cp310-manylinux_2_31_x86_64.whl")
    version("7.7.0-py311", sha256="b167faa03f4c12193ed7a5dabae0d7544432b50503ad800d97288a0aef5bd909", expand=False, url="https://files.pythonhosted.org/packages/96/21/0e31998c41dd5e83bd94c3bacc49a566eaf20555982bb7efae0c9a09a716/cadquery_ocp-7.7.0-cp311-cp311-manylinux_2_31_x86_64.whl")
    version("7.7.0-py38", sha256="cfa16341b229ec0f650a11ce43888be8a2688d39f58c4c762b7a85011785e773", expand=False, url="https://files.pythonhosted.org/packages/a9/bc/fbe4df5fa2c56449fbfde402878100dfe830ad3445b6233cda9ca3069246/cadquery_ocp-7.7.0-cp38-cp38-manylinux_2_31_x86_64.whl")
    version("7.7.0-py39", sha256="01c81b233ada506950af3dada63b9e694786ff6442fbecffcffe20719a500d8d", expand=False, url="https://files.pythonhosted.org/packages/ab/d7/1e23ef16727b7bda822aa3b39feaef3ee80651930a64f84c904c8cd9db09/cadquery_ocp-7.7.0-cp39-cp39-manylinux_2_31_x86_64.whl")
    version("7.7.0a0-py310", sha256="e4559c4e64871f5cff758e03c3edca5b5f50f8dfcb7c0c956c9a86f4e950c307", expand=False, url="https://files.pythonhosted.org/packages/5f/48/e995d09621d95c290d5625dc938457dbe28a8cc4a420f0108435a4d56c5d/cadquery_ocp-7.7.0a0-cp310-cp310-manylinux_2_31_x86_64.whl")
    version("7.7.0a0-py311", sha256="7e8a3dfb98aef4f049c3a3d57b232f1b4d279fdd3b343f858305ab034fee5044", expand=False, url="https://files.pythonhosted.org/packages/bb/38/b2db0f9dbdfdafff0aaf306253371e91d2332cb987c5733df8998297f41e/cadquery_ocp-7.7.0a0-cp311-cp311-manylinux_2_31_x86_64.whl")
    version("7.7.0a0-py38", sha256="7878408c066bbc588d17086a96a92fb80b021abc2e64ddf133e30f597fe93050", expand=False, url="https://files.pythonhosted.org/packages/49/0c/cebaac9e3cd5282d8538d477d81cc2b52cb27f9859a86de487858764dcbe/cadquery_ocp-7.7.0a0-cp38-cp38-manylinux_2_31_x86_64.whl")
    version("7.7.0a0-py39", sha256="a7f8d1d36b990fa6f29d336d873763f0b3983ad76cd6f28f4f10876b4ec3b7bc", expand=False, url="https://files.pythonhosted.org/packages/c9/2d/31d328ca37244b2e94fe90e486d93558b835af67ac217061d0ebdb9b739c/cadquery_ocp-7.7.0a0-cp39-cp39-manylinux_2_31_x86_64.whl")
    version("7.7.1-py310", sha256="efc52b7503c28d25b224249b453886aa98ef4a03b9426fe96e8dac56340a074d", expand=False, url="https://files.pythonhosted.org/packages/4a/49/3169c76f9c567b1919b72a56f5842056dd2ccae28fcf7cbbb304ba788eef/cadquery_ocp-7.7.1-cp310-cp310-manylinux_2_35_x86_64.whl")
    version("7.7.1-py311", sha256="83457789a3045f1c9ab4ee9d00b7169433e567705256637625c2620648029e4d", expand=False, url="https://files.pythonhosted.org/packages/73/ed/3c5f722d1fa78e6d8c8da276c47916faecdffdf7cc005270abb923e46063/cadquery_ocp-7.7.1-cp311-cp311-manylinux_2_35_x86_64.whl")
    version("7.7.1-py38", sha256="6b38e857525f2b170c0fdf14770169a822497e2a1afa6c78434021fffd4f63c3", expand=False, url="https://files.pythonhosted.org/packages/eb/2a/0240cd17d676d2a44ae2e2081630ec3fa101549d17688cdf24a93be491e2/cadquery_ocp-7.7.1-cp38-cp38-manylinux_2_35_x86_64.whl")
    version("7.7.1-py39", sha256="3fd169a342a9ae9e7da5e5b1ad0b8820770f3d81c91f808126a8fbf47c1cb98a", expand=False, url="https://files.pythonhosted.org/packages/06/97/c3ac73d5bea69c1381e177243a43e3392b18ab2996f9758705cf8683b9e5/cadquery_ocp-7.7.1-cp39-cp39-manylinux_2_35_x86_64.whl")
    version("7.7.2-py310", sha256="35e2c8ca923e4ba77b833357eb14c7e8a939f17285ef6acde7c26961989a8dfe", expand=False, url="https://files.pythonhosted.org/packages/b7/c8/ca16b397406352b38f98e1ac22fc7fc93224748006dbf7bffff1f9237c96/cadquery_ocp-7.7.2-cp310-cp310-manylinux_2_35_x86_64.whl")
    version("7.7.2-py311", sha256="2be9408551c03e1c715e3b158b41ce458178ecf530ba644e3e884a5989feb611", expand=False, url="https://files.pythonhosted.org/packages/ee/ce/e38d7fb8ee5f3d5c57b2fe8914bea8e8307b693bb07b8c8d87786824d54e/cadquery_ocp-7.7.2-cp311-cp311-manylinux_2_35_x86_64.whl")
    version("7.7.2-py312", sha256="7ac2d83b4f4b3d7c35421a1d9f8fec2adc73b6ed6cac50c1ffcede5552e38e9b", expand=False, url="https://files.pythonhosted.org/packages/c7/78/f81639f0cd4e899ed2cee705a255ef1abe8d97b06f6f3f4b6aaf8d4b2a5d/cadquery_ocp-7.7.2-cp312-cp312-manylinux_2_35_x86_64.whl")
    version("7.7.2-py38", sha256="73183f141514e507c45a1e4ba1d25f1fdc604b20dd42bed7c8168f468632686b", expand=False, url="https://files.pythonhosted.org/packages/7e/e9/66ea9e871c0d6ab7d5fe12db59a642fadf3603ee2a318818482d4aad926f/cadquery_ocp-7.7.2-cp38-cp38-manylinux_2_35_x86_64.whl")
    version("7.7.2-py39", sha256="9f6c601d1db66353f0ef7c63fde70411573e917c16fb4c7cb5d92ed85b72f154", expand=False, url="https://files.pythonhosted.org/packages/ea/f8/7350acdffdfb437045caab9c3b7c4a73f85b8c7cfe95f39ca6656fe5ca68/cadquery_ocp-7.7.2-cp39-cp39-manylinux_2_35_x86_64.whl")
    version("7.7.2.2b2-py310", sha256="2408fe9c7ca1e0d094b0a553e65ad7255863476de3ff12c2290582713bd484b8", expand=False, url="https://files.pythonhosted.org/packages/23/d0/32ad904b01aaef0684d02e344368ffcbd17e2a3ffa64e673a8bc1ba74ba1/cadquery_ocp-7.7.2.2b2-cp310-cp310-manylinux_2_31_x86_64.whl")
    version("7.7.2.2b2-py311", sha256="d6b4be2ed2fbd4546d833dd2edd9014e937d8a5f942047efbd128483c1c9d5fe", expand=False, url="https://files.pythonhosted.org/packages/66/2b/ad373fd20a56992b8cd0c85383582c5791ac121c64012c72b018e9955d29/cadquery_ocp-7.7.2.2b2-cp311-cp311-manylinux_2_31_x86_64.whl")
    # Known-good wheel for Python 3.10
    version("7.8.1.1.post1-py310", sha256="b843adfff9014011c32ec68028055e558023a1d567a3b27bcd19d2e97f35ac73", expand=False, url="https://files.pythonhosted.org/packages/2e/0d/14f9254c1a821e77affe2426b2b0cca99b9437362840578bd8f2a4fb651b/cadquery_ocp-7.8.1.1.post1-cp310-cp310-manylinux_2_31_x86_64.whl")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.10:3.14", type=("build", "run"))
    # Use Python VTK wheels to satisfy libvtkWrappingPythonCore at runtime
    depends_on("py-vtk", type=("run"))
    # X/GL runtime libraries required by the wheel at import time
    depends_on("libx11", type=("run"))
    depends_on("libxrender", type=("run"))
    depends_on("libxcb", type=("run"))
    depends_on("libxau", type=("run"))
    depends_on("libxdmcp", type=("run"))
    depends_on("mesa", type=("run"))

    
    depends_on("python@3.10", when="@7.5.3.0-py310", type=("build", "run"))
    depends_on("python@3.8", when="@7.5.3.0-py38", type=("build", "run"))
    depends_on("python@3.9", when="@7.5.3.0-py39", type=("build", "run"))
    depends_on("python@3.10", when="@7.6.3-py310", type=("build", "run"))
    depends_on("python@3.8", when="@7.6.3-py38", type=("build", "run"))
    depends_on("python@3.9", when="@7.6.3-py39", type=("build", "run"))
    depends_on("python@3.10", when="@7.6.3a0-py310", type=("build", "run"))
    depends_on("python@3.8", when="@7.6.3a0-py38", type=("build", "run"))
    depends_on("python@3.9", when="@7.6.3a0-py39", type=("build", "run"))
    depends_on("python@3.10", when="@7.7.0-py310", type=("build", "run"))
    depends_on("python@3.11", when="@7.7.0-py311", type=("build", "run"))
    depends_on("python@3.8", when="@7.7.0-py38", type=("build", "run"))
    depends_on("python@3.9", when="@7.7.0-py39", type=("build", "run"))
    depends_on("python@3.10", when="@7.7.0a0-py310", type=("build", "run"))
    depends_on("python@3.11", when="@7.7.0a0-py311", type=("build", "run"))
    depends_on("python@3.8", when="@7.7.0a0-py38", type=("build", "run"))
    depends_on("python@3.9", when="@7.7.0a0-py39", type=("build", "run"))
    depends_on("python@3.10", when="@7.7.1-py310", type=("build", "run"))
    depends_on("python@3.11", when="@7.7.1-py311", type=("build", "run"))
    depends_on("python@3.8", when="@7.7.1-py38", type=("build", "run"))
    depends_on("python@3.9", when="@7.7.1-py39", type=("build", "run"))
    depends_on("python@3.10", when="@7.7.2-py310", type=("build", "run"))
    depends_on("python@3.11", when="@7.7.2-py311", type=("build", "run"))
    depends_on("python@3.12", when="@7.7.2-py312", type=("build", "run"))
    depends_on("python@3.8", when="@7.7.2-py38", type=("build", "run"))
    depends_on("python@3.9", when="@7.7.2-py39", type=("build", "run"))
    # Ensure ABI-compatible VTK for OCP 7.7.* (expects 9.2.x)
    depends_on("py-vtk@9.2.4:9.2.6", when="@7.7.0:7.7.999", type=("run"))
    # OCP 7.8.1.1.post1 for py310 expects VTK 9.3.1
    depends_on("py-vtk@9.3.1", when="@7.8.1.1.post1-py310", type=("run"))
    depends_on("python@3.10", when="@7.7.2.2b2-py310", type=("build", "run"))
    depends_on("python@3.11", when="@7.7.2.2b2-py311", type=("build", "run"))
    depends_on("python@3.10", when="@7.8.1.1.post1-py310", type=("build", "run"))

    def install(self, spec, prefix):
            # Standard wheel install; avoid writing to container paths here.
            super(PyCadqueryOcp, self).install(spec, prefix)

            # Create a safe, unstripped copy of the wheel runtime under
            # /opt/spack-environment so it is included in the final image and
            # not processed by the strip step that targets /opt/view.
            try:
                py_version_short = spec["python"].version.up_to(2)
                site_dir = join_path(prefix, "lib", f"python{py_version_short}", "site-packages")
                ocp_src = join_path(site_dir, "OCP")
                ocp_libs_src = join_path(site_dir, "cadquery_ocp.libs")
                vtkmodules_src = join_path(site_dir, "vtkmodules")

                safe_site = join_path("/opt/spack-environment", "ocp-safe", f"python{py_version_short}", "site-packages")
                safe_ocp = join_path(safe_site, "OCP")
                safe_ocp_libs = join_path(safe_site, "cadquery_ocp.libs")
                safe_vtkmodules = join_path(safe_site, "vtkmodules")

                def copy_deref_tree(src_root, dst_root):
                    if not os.path.isdir(src_root):
                        return
                    mkdirp(dst_root)
                    for current_dir, _, filenames in os.walk(src_root):
                        rel_dir = os.path.relpath(current_dir, src_root)
                        target_dir = join_path(dst_root, rel_dir) if rel_dir != "." else dst_root
                        mkdirp(target_dir)
                        for filename in filenames:
                            src_path = join_path(current_dir, filename)
                            dst_path = join_path(target_dir, filename)
                            real_src = os.path.realpath(src_path)
                            if os.path.islink(dst_path) or os.path.exists(dst_path):
                                try:
                                    os.remove(dst_path)
                                except Exception:
                                    pass
                            shutil.copy2(real_src, dst_path)

                # Populate safe site with dereferenced copies
                copy_deref_tree(ocp_src, safe_ocp)
                if os.path.isdir(ocp_libs_src):
                    copy_deref_tree(ocp_libs_src, safe_ocp_libs)
                if os.path.isdir(vtkmodules_src):
                    copy_deref_tree(vtkmodules_src, safe_vtkmodules)

                # Drop a .pth file into our own site-packages so Python inserts the
                # safe site at sys.path[0] on interpreter startup.
                try:
                    pth_path = os.path.join(site_dir, "zz-ocp-safe-first.pth")
                    with open(pth_path, "w", encoding="utf-8") as f:
                        f.write(f"import sys; sys.path.insert(0, {safe_site!r})\n")
                except Exception:
                    pass
            except Exception:
                # Best-effort: if anything fails, leave default layout
                pass

    def setup_run_environment(self, env):
            # Prefer the safe site that contains dereferenced, unstripped files
            py_version_short = self.spec["python"].version.up_to(2)
            safe_site = os.path.join("/opt/spack-environment", "ocp-safe", f"python{py_version_short}", "site-packages")
            env.prepend_path("PYTHONPATH", safe_site)
            env.prepend_path("LD_LIBRARY_PATH", os.path.join(safe_site, "OCP"))
            env.prepend_path("LD_LIBRARY_PATH", os.path.join(safe_site, "vtkmodules"))

            # Ensure py-vtk shared libs are discoverable at runtime
            if "py-vtk" in self.spec:
                pyvtk = self.spec["py-vtk"].prefix
                # Add standard lib dirs
                for libdir in ("lib", "lib64"):
                    env.prepend_path("LD_LIBRARY_PATH", os.path.join(pyvtk, libdir))
                # Also add wheel .so location under site-packages/vtkmodules
                py_version_short = self.spec["python"].version.up_to(2)
                vtk_site = os.path.join(
                    pyvtk,
                    "lib",
                    f"python{py_version_short}",
                    "site-packages",
                    "vtkmodules",
                )
                env.prepend_path("LD_LIBRARY_PATH", vtk_site)
            # Add X11 and GL libraries needed by OCP's OpenGL bindings
            for dep in ("libx11", "libxrender", "libxcb", "libxau", "libxdmcp", "mesa"):
                if dep in self.spec:
                    for libdir in ("lib", "lib64"):
                        env.prepend_path("LD_LIBRARY_PATH", os.path.join(self.spec[dep].prefix, libdir))

    # Ensure real files (not symlinks) are placed into the view for OCP and
    # its sibling wheels, so later container steps don't strip underlying
    # symlink targets and break ELF alignment.
    def add_files_to_view(self, view, merge_map, skip_if_exists=True):
        # Partition: force copy for wheel runtime dirs, otherwise defer to base
        tokens = [
            f"{os.sep}site-packages{os.sep}OCP{os.sep}",
            f"{os.sep}site-packages{os.sep}cadquery_ocp.libs{os.sep}",
            f"{os.sep}site-packages{os.sep}vtkmodules{os.sep}",
        ]
        targeted = {}
        others = {}
        for src, dst in merge_map.items():
            if any(t in src for t in tokens):
                targeted[src] = dst
            else:
                others[src] = dst

        if others:
            super(PyCadqueryOcp, self).add_files_to_view(view, others, skip_if_exists)

        for src, dst in targeted.items():
            if skip_if_exists and os.path.lexists(dst):
                continue
            mkdirp(os.path.dirname(dst))
            sview.view_copy(os.path.realpath(src), dst, view=view, spec=self.spec)
# {'vtk==9.2.6': ['7.7.2.2b2-py310', '7.7.2.2b2-py311'], 'vtk==9.3.1': ['7.8.1.0-py310', '7.8.1.0-py311', '7.8.1.0-py312', '7.8.1.1-py310', '7.8.1.1-py311', '7.8.1.1-py312', '7.8.1.1.post1-py310', '7.8.1.1.post1-py311', '7.8.1.1.post1-py312'], 'cadquery_vtk==9.3.1': ['7.8.1.0-py313', '7.8.1.1-py313', '7.8.1.1.post1-py313']}