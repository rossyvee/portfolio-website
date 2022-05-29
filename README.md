# Photo Gallery

```
          <div class="form-group mb-2">
            <label for="category" class="label mb-1">Category</label>
            <select name="category" id="category" required class="form-control">
              <option value="">--select--</option>
              {% if categories %}
                  {% for category in categories %}
                    <option>{{category.name}}</option>
                  {% endfor %}
              {% endif %}
            </select>
          </div>

          <div class="form-group mb-2">
            <label for="location" class="label mb-1">Location</label>
            <select name="location" id="location" required class="form-control">
              <option value="">--select--</option>
              {% if locations %}
                  {% for location in locations %}
                    <option>{{location.name}}</option>
                  {% endfor %}
              {% endif %}
            </select>
          </div>

          <div class="form-group mb-2">
            <label for="name" class="label mb-1">Name</label>
            <input type="text" id="name" name="name"  class="form-control" required/>
          </div>

          <div class="form-group mb-2">
            <label for="description" class="label mb-1">Description</label>
            <input type="text" id="description" name="description" class="form-control" required/>
          </div>

          <div class="form-group mb-2">
            <label for="image" class="label mb-1">Image</label>
            <input type="file"  id="image" name="image" class="form-control" required/>
          </div>
```