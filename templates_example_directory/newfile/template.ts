/**
 * Copyright (C) {{ year }} {{ projectAuthor }}
 * See end of file for extended copyright information
 */

function createTemplate(): string {
    return "{{ projectName }} created";
}

const result = createTemplate();
console.log(result);

/**
 * Copyright (C) {{ year }} {{ projectAuthor }}
 * 
 * {{ projectName }}
 * {{ projectDescription }}
 *
 * {% if licenseName == "All Rights Reserved" %}All Rights Reserved{% else %}This code is licensed under the {{ licenseName }}.
 * Please see the LICENSE file in the root directory of this project for the full license details.{% endif %}
 */
